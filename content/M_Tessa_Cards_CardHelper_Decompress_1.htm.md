# CardHelper.Decompress(IStorageObjectProvider) - метод
Выполняет распаковку пакета карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Card Decompress(
    	IStorageObjectProvider storageObjectProvider
    )
VB __Копировать
     Public Shared Function Decompress ( 
    	storageObjectProvider As IStorageObjectProvider
    ) As Card
C++ __Копировать
     public:
    static Card^ Decompress(
    	IStorageObjectProvider^ storageObjectProvider
    )
F# __Копировать
     static member Decompress : 
            storageObjectProvider : IStorageObjectProvider -> Card 
#### Параметры
storageObjectProvider
[IStorageObjectProvider](T_Tessa_Platform_Storage_IStorageObjectProvider.htm)
     Объект, предоставляющий доступ к хранилищу, содержащему упакованные данные пакета карточки. 
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
