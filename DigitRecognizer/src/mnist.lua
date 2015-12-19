require 'csvigo';
require 'torch';
require 'nn';

local function load_data(file_path)
  local csv_data = csvigo.load({path=file_path, mode = 'large'})
  local no_of_ins = #csv_data - 1
  local total_no_of_pixels = #csv_data[1]
  local data = torch.Tensor(no_of_ins, total_no_of_pixels)
  for ins_no, ins in ipairs(csv_data) do
    if ins_no > 1 then
      data[ins_no - 1] = torch.Tensor(ins)
    end
  end
  return data
end

local function load_train_data()
  local data = load_data('../train.csv')
  local no_of_ins, total_no_of_pixels = data:size(1), data:size(2) - 1
  local train_data, train_labels = data[{{}, {2, total_no_of_pixels}}], data[{{}, {1}}]
  local no_of_pixels = math.sqrt(total_no_of_pixels)
  train_data = train_data:resize(no_of_ins, no_of_pixels, no_of_pixels)
  return train_data, train_labels
end

local function load_test_data()
  local test_data = load_data('../test.csv')
  local no_of_ins, total_no_of_pixels = data:size(1), data:size(2)
  local no_of_pixels = math.sqrt(total_no_of_pixels)
  test_data = test_data:resize(no_of_ins, no_of_pixels, no_of_pixels)
  return test_data
end

local function get_trained_nn()
  local net = nn.Sequential()
  net:add(nn.Sp)
end

local function main()
  local train_data, train_labels = load_train_data()
  local possible_classes = {'1','2','3','4','5','6','7','8','9','10'}

end

main()
