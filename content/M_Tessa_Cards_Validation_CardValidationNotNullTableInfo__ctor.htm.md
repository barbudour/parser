# CardValidationNotNullTableInfo - конструктор
Создаёт экземпляр класса с указанием значений его свойств.
## __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardValidationNotNullTableInfo(
    	CardTypeValidator validator,
    	CardMetadataSection section,
    	CardType cardType,
    	Card instance,
    	CardStoreMode storeMode
    )
VB __Копировать
     Public Sub New ( 
    	validator As CardTypeValidator,
    	section As CardMetadataSection,
    	cardType As CardType,
    	instance As Card,
    	storeMode As CardStoreMode
    )
C++ __Копировать
     public:
    CardValidationNotNullTableInfo(
    	CardTypeValidator^ validator, 
    	CardMetadataSection^ section, 
    	CardType^ cardType, 
    	Card^ instance, 
    	CardStoreMode storeMode
    )
F# __Копировать
     new : 
            validator : CardTypeValidator * 
            section : CardMetadataSection * 
            cardType : CardType * 
            instance : Card * 
            storeMode : CardStoreMode -> CardValidationNotNullTableInfo
#### Параметры
validator [CardTypeValidator](T_Tessa_Cards_CardTypeValidator.htm)
    Валидатор, инициировавший проверку.
section [CardMetadataSection](T_Tessa_Cards_Metadata_CardMetadataSection.htm)
    Секция, в которой требуется проверить наличие строк.
cardType [CardType](T_Tessa_Cards_CardType.htm)
    Тип карточки, файла или задания, к которому принадлежит секция.
instance [Card](T_Tessa_Cards_Card.htm)
     Проверяемый объект, по которому могут быть получены секции и идентификатор. Может быть объектом карточки, файла или задания. 
storeMode [CardStoreMode](T_Tessa_Cards_CardStoreMode.htm)
     Режим сохранения карточки. Поскольку instance может быть заданием, то режим сохранения определяем отдельным свойством. 
## __См. также
#### Ссылки
[CardValidationNotNullTableInfo -
](T_Tessa_Cards_Validation_CardValidationNotNullTableInfo.htm)
[Tessa.Cards.Validation - пространство имён](N_Tessa_Cards_Validation.htm)
