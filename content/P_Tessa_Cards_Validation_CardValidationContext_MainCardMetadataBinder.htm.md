# CardValidationContext.MainCardMetadataBinder - свойство
Объект, выполняющий действия с основной карточкой, для которой выполняется
валидация.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ICardMetadataBinder MainCardMetadataBinder { get; set; }
VB __Копировать
     Public Property MainCardMetadataBinder As ICardMetadataBinder
    	Get
    	Set
C++ __Копировать
     public:
    virtual property ICardMetadataBinder^ MainCardMetadataBinder {
    	ICardMetadataBinder^ get () sealed;
    	void set (ICardMetadataBinder^ value) sealed;
    }
F# __Копировать
     abstract MainCardMetadataBinder : ICardMetadataBinder with get, set
    override MainCardMetadataBinder : ICardMetadataBinder with get, set
#### Значение свойства
[ICardMetadataBinder](T_Tessa_Cards_Metadata_ICardMetadataBinder.htm)
#### Реализации
[ICardValidationContext.MainCardMetadataBinder](P_Tessa_Cards_Validation_ICardValidationContext_MainCardMetadataBinder.htm)  
##  __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[CardValidationContext - ](T_Tessa_Cards_Validation_CardValidationContext.htm)
[Tessa.Cards.Validation - пространство имён](N_Tessa_Cards_Validation.htm)
[Tessa.Platform.ObjectSealedException]
