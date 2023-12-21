# CardHelper.CreateSectionRows - метод
Создаёт объект, содержащий коллекцию пустых строк коллекционных и древовидных
секций, упорядоченных по имени секции.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static StringDictionaryStorage<CardRow> CreateSectionRows(
    	int capacity = 0
    )
VB __Копировать
     Public Shared Function CreateSectionRows ( 
    	Optional capacity As Integer = 0
    ) As StringDictionaryStorage(Of CardRow)
C++ __Копировать
     public:
    static StringDictionaryStorage<CardRow^>^ CreateSectionRows(
    	int capacity = 0
    )
F# __Копировать
     static member CreateSectionRows : 
            ?capacity : int 
    (* Defaults:
            let _capacity = defaultArg capacity 0
    *)
    -> StringDictionaryStorage<CardRow> 
#### Параметры
capacity [Int32](https://learn.microsoft.com/dotnet/api/system.int32)
(Optional)
     Начальная вместимость созданной коллекции или 0, если используется вместимость по умолчанию. 
#### Возвращаемое значение
[StringDictionaryStorage](T_Tessa_Platform_Storage_StringDictionaryStorage_1.htm)<[CardRow](T_Tessa_Cards_CardRow.htm)>  
Созданный объект, содержащий коллекцию пустых строк коллекционных и
древовидных секций, упорядоченных по имени секции.
## __См. также
#### Ссылки
[CardHelper - ](T_Tessa_Cards_CardHelper.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
