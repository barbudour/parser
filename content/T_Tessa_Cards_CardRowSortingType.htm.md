# CardRowSortingType - перечисление
Тип сортировки строк для коллекционной или древовидной секции, которая
используется при вставке и удалении строк в процессе сохранения карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public enum CardRowSortingType
VB __Копировать
     Public Enumeration CardRowSortingType
C++ __Копировать
     public enum class CardRowSortingType
F# __Копировать
     type CardRowSortingType
##  __Члены
Auto| 0|  Сортировка производится автоматически при необходимости. При этом
сортируются только строки древовидной секции с учётом порядка следования
родительских строк по отношению к дочерним.  
---|---|---  
Manual| 1|  Порядок сортировки устанавливается вручную для каждой строки через
свойство [SortingOrder](P_Tessa_Cards_CardRow_SortingOrder.htm). Для
древовидных секций строки при этом будут отсортированы без учёта порядка
следования родительских строк по отношению к дочерним.  
## __См. также
#### Ссылки
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
