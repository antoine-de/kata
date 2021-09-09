# run this with elixir yahtzee.exs <combinaison> <dices>
# for example:
# elixir yahtzee.exs pair 1 4 3 4 2

defmodule Yahtzee do
  defp dice_value({d, _}) when d <= 6, do: d

  defp sort_and_validate([_d1, _d2, _d3, _d4, _d5] = dices),
    do:
      dices
      |> Enum.map(&Integer.parse/1)
      |> Enum.map(&dice_value/1)
      |> Enum.sort()
      |> Enum.reverse()

  def read_args([combinaison | dices]) do
    {
      combinaison |> String.to_existing_atom(),
      dices |> sort_and_validate
    }
  end

  def get_value(combinaison, dices),
    do:
      combinaison
      |> matching_dices(dices)
      |> Enum.sum()

  defp matching_dices(:pair, [x, x | _]), do: [x, x]
  defp matching_dices(:pair, [_ | rest]), do: matching_dices(:pair, rest)
  defp matching_dices(:pair, []), do: []

  defp matching_dices(:brelan, dices), do: dices |> n_of_a_kind(3)
  defp matching_dices(:square, dices), do: dices |> n_of_a_kind(4)

  defp matching_dices(:yahtzee, [x, x, x, x, x]), do: [x, x, x, x, x]
  defp matching_dices(:yahtzee, _), do: []

  defp matching_dices(:chance, dices), do: dices

  defp matching_dices(:ones, dices), do: Enum.filter(dices, &(&1 == 1))
  defp matching_dices(:twos, dices), do: Enum.filter(dices, fn d -> d == 2 end)
  defp matching_dices(:threes, dices), do: Enum.filter(dices, fn d -> d == 3 end)
  defp matching_dices(:fours, dices), do: Enum.filter(dices, fn d -> d == 4 end)
  defp matching_dices(:fives, dices), do: Enum.filter(dices, fn d -> d == 5 end)
  defp matching_dices(:sixes, dices), do: Enum.filter(dices, fn d -> d == 6 end)

  # for straight both implem works, I like the forwardness of the first one :D
  # defp matching_dices(:straight, [d1, d2, d3, d4, d5] = dices)
  #    when d1 == d2 + 1 and
  #           d2 == d3 + 1 and
  #           d3 == d4 + 1 and
  #           d4 == d5 + 1,
  #    do: dices
  # defp matching_dices(:straight, _), do: []
  defp matching_dices(:straight, dices) do
    dices
    |> Enum.chunk_every(2, 1, :discard)
    |> Enum.all?(fn [x, y] -> x == y + 1 end)
    |> case do
      true -> dices
      _ -> []
    end
  end

  defp matching_dices(:full, [x, x, y, y, y] = dices), do: dices
  defp matching_dices(:full, [x, x, x, y, y] = dices), do: dices
  defp matching_dices(:full, _), do: []

  # generic way to do pair/brelan/square and yahtzee
  defp n_of_a_kind(dices, n),
    do:
      dices
      |> Enum.chunk_by(& &1)
      |> Enum.filter(&(length(&1) == n))
      |> List.first([])
end

{combinaison, dices} = Yahtzee.read_args(System.argv())
value = Yahtzee.get_value(combinaison, dices)
IO.puts("value for (#{combinaison} / #{inspect(dices)}) = #{value}")
