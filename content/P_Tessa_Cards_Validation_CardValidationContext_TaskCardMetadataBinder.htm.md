# CardValidationContext.TaskCardMetadataBinder - свойство
Объект, выполняющий действия с карточкой задания, для которой выполняется
валидация, или null, если задание завершается без данных карточки или
валидация задания не выполняется.
## __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ICardMetadataBinder TaskCardMetadataBinder { get; set; }
VB __Копировать
     Public Property TaskCardMetadataBinder As ICardMetadataBinder
    	Get
    	Set
C++ __Копировать
     public:
    virtual property ICardMetadataBinder^ TaskCardMetadataBinder {
    	ICardMetadataBinder^ get () sealed;
    	void set (ICardMetadataBinder^ value) sealed;
    }
F# __Копировать
     abstract TaskCardMetadataBinder : ICardMetadataBinder with get, set
    override TaskCardMetadataBinder : ICardMetadataBinder with get, set
#### Значение свойства
[ICardMetadataBinder](T_Tessa_Cards_Metadata_ICardMetadataBinder.htm)
#### Реализации
[ICardValidationContext.TaskCardMetadataBinder](P_Tessa_Cards_Validation_ICardValidationContext_TaskCardMetadataBinder.htm)  
##  __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[CardValidationContext - ](T_Tessa_Cards_Validation_CardValidationContext.htm)
[Tessa.Cards.Validation - пространство имён](N_Tessa_Cards_Validation.htm)
[Tessa.Platform.ObjectSealedException]
