# CardErrorDetailWriter - конструктор
Создаёт экземпляр класса с указанием его зависимостей.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardErrorDetailWriter(
    	ICardFileManager cardFileManagerWithoutTransaction,
    	ICardMetadata cardMetadata
    )
VB __Копировать
     Public Sub New ( 
    	cardFileManagerWithoutTransaction As ICardFileManager,
    	cardMetadata As ICardMetadata
    )
C++ __Копировать
     public:
    CardErrorDetailWriter(
    	ICardFileManager^ cardFileManagerWithoutTransaction, 
    	ICardMetadata^ cardMetadata
    )
F# __Копировать
     new : 
            cardFileManagerWithoutTransaction : ICardFileManager * 
            cardMetadata : ICardMetadata -> CardErrorDetailWriter
#### Параметры
cardFileManagerWithoutTransaction
[ICardFileManager](T_Tessa_Cards_ICardFileManager.htm)
     Объект для управления файлами карточки. На сервере это должен быть объект без транзакций, например, [ExtendedWithoutTransaction](F_Tessa_Cards_CardRepositoryNames_ExtendedWithoutTransaction.htm). На клиенте это реализация [ICardFileManager](T_Tessa_Cards_ICardFileManager.htm) по умолчанию. 
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
    Метаинформация по типам карточек.
##  __См. также
#### Ссылки
[CardErrorDetailWriter - ](T_Tessa_Cards_CardErrorDetailWriter.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
