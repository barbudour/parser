# CardFileContainer - конструктор
Создаёт экземпляр класса с указанием значений его свойств.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardFileContainer(
    	Card card,
    	IFileContainer fileContainer,
    	ICardFileManager manager,
    	ValidationResult creationResult
    )
VB __Копировать
     Public Sub New ( 
    	card As Card,
    	fileContainer As IFileContainer,
    	manager As ICardFileManager,
    	creationResult As ValidationResult
    )
C++ __Копировать
     public:
    CardFileContainer(
    	Card^ card, 
    	IFileContainer^ fileContainer, 
    	ICardFileManager^ manager, 
    	ValidationResult^ creationResult
    )
F# __Копировать
     new : 
            card : Card * 
            fileContainer : IFileContainer * 
            manager : ICardFileManager * 
            creationResult : ValidationResult -> CardFileContainer
#### Параметры
card [Card](T_Tessa_Cards_Card.htm)
    Карточка.
fileContainer [IFileContainer](T_Tessa_Files_IFileContainer.htm)
    Файлы, относящиеся к карточке.
manager [ICardFileManager](T_Tessa_Cards_ICardFileManager.htm)
    Объект, который управляет созданным контейнером.
creationResult
[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm)
    Результат создания текущего объекта. Может содержать ошибки, связанные с получением файлов.
##  __См. также
#### Ссылки
[CardFileContainer - ](T_Tessa_Cards_CardFileContainer.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
