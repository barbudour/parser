# CardHelper.Compress - метод
Выполняет упаковку пакета карточки. Заданный декоратор становится непригоден к
использованию.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Dictionary<string, Object> Compress(
    	Card card
    )
VB __Копировать
     Public Shared Function Compress ( 
    	card As Card
    ) As Dictionary(Of String, Object)
C++ __Копировать
     public:
    static Dictionary<String^, Object^>^ Compress(
    	Card^ card
    )
F# __Копировать
     static member Compress : 
            card : Card -> Dictionary<string, Object> 
#### Параметры
card [Card](T_Tessa_Cards_Card.htm)
    Декоратор карточки, для хранилища которого необходимо выполнить упаковку.
#### Возвращаемое значение
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>  
Хранилище, содержащее упакованные данные пакета карточки. Такие данные
несовместимы с декораторами.
##  __Заметки
Для распаковки пакета карточки можно использовать метод
[Decompress(IStorageObjectProvider)](M_Tessa_Cards_CardHelper_Decompress_1.htm).
## __См. также
#### Ссылки
[CardHelper - ](T_Tessa_Cards_CardHelper.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
