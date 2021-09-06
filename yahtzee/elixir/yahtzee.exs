# run this with elixir yahtzee.exs <combinaison> <dices>
# for example:
# elixir yahtzee.exs pair 1 4 3 4 2

defmodule Yahtzee do
  def _dice_value({d, _}) when d <= 6, do: d

  def _sort_and_validate([_d1, _d2, _d3, _d4, _d5] = dices),
    do:
      dices
      |> Enum.map(&Integer.parse/1)
      |> Enum.map(&_dice_value/1)
      |> Enum.sort()
      |> Enum.reverse()

  def read_args([combinaison | dices]) do
    {
      combinaison |> String.to_existing_atom(),
      dices |> _sort_and_validate
    }
  end

  def get_value(combinaison, dices),
    do:
      combinaison
      |> _matching_dices(dices)
      |> Enum.sum()

  def _matching_dices(:pair, [x, x | _]), do: [x, x]
  def _matching_dices(:pair, [_ | rest]), do: _matching_dices(:pair, rest)
  def _matching_dices(:pair, []), do: []

  def _matching_dices(:brelan, [x, x, x | _]), do: [x, x, x]
  def _matching_dices(:brelan, [_ | rest]), do: _matching_dices(:brelan, rest)
  def _matching_dices(:brelan, []), do: []

  def _matching_dices(:square, [x, x, x, x | _]), do: [x, x, x, x]
  def _matching_dices(:square, [_ | rest]), do: _matching_dices(:square, rest)
  def _matching_dices(:square, []), do: []

  def _matching_dices(:yahtzee, [x, x, x, x, x]), do: [x, x, x, x, x]
  def _matching_dices(:yahtzee, _), do: []

  def _matching_dices(:chance, dices), do: dices

  def _matching_dices(:ones, dices), do: Enum.filter(dices, fn d -> d == 1 end)
  def _matching_dices(:twos, dices), do: Enum.filter(dices, fn d -> d == 2 end)
  def _matching_dices(:threes, dices), do: Enum.filter(dices, fn d -> d == 3 end)
  def _matching_dices(:fours, dices), do: Enum.filter(dices, fn d -> d == 4 end)
  def _matching_dices(:fives, dices), do: Enum.filter(dices, fn d -> d == 5 end)
  def _matching_dices(:sixes, dices), do: Enum.filter(dices, fn d -> d == 6 end)

  # for straight both implem works, I like the forwardness of the first one :D
  # def _matching_dices(:straight, [d1, d2, d3, d4, d5] = dices)
  #    when d1 == d2 + 1 and
  #           d2 == d3 + 1 and
  #           d3 == d4 + 1 and
  #           d4 == d5 + 1,
  #    do: dices
  # def _matching_dices(:straight, _), do: []
  def _matching_dices(:straight, dices) do
    dices
    |> Enum.chunk_every(2, 1, :discard)
    |> Enum.all?(fn [x, y] -> x == y + 1 end)
    |> case do
      true -> dices
      _ -> []
    end
  end

  def _matching_dices(:full, [x, x, y, y, y] = dices), do: dices
  def _matching_dices(:full, [x, x, x, y, y] = dices), do: dices
  def _matching_dices(:full, _), do: []
end

{combinaison, dices} = Yahtzee.read_args(System.argv())
value = Yahtzee.get_value(combinaison, dices)
IO.puts("value for (#{combinaison} / #{inspect(dices)}) = #{value}")
