# CardHelper.Decompress(Dictionary<String, Object>) - метод
Выполняет распаковку пакета карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Card Decompress(
    	Dictionary<string, Object> storage
    )
VB __Копировать
     Public Shared Function Decompress ( 
    	storage As Dictionary(Of String, Object)
    ) As Card
C++ __Копировать
     public:
    static Card^ Decompress(
    	Dictionary<String^, Object^>^ storage
    )
F# __Копировать
     static member Decompress : 
            storage : Dictionary<string, Object> -> Card 
#### Параметры
storage
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>
    Хранилище, содержащее упакованные данные пакета карточки.
#### Возвращаемое значение
[Card](T_Tessa_Cards_Card.htm)  
Декоратор для пакета карточки, полученный в результате распаковки.
##  __Заметки
Для упаковки пакета карточки можно использовать метод
[Compress(Card)](M_Tessa_Cards_CardHelper_Compress.htm).
## __См. также
#### Ссылки
[CardHelper - ](T_Tessa_Cards_CardHelper.htm)
[Decompress - перегрузка](Overload_Tessa_Cards_CardHelper_Decompress.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
