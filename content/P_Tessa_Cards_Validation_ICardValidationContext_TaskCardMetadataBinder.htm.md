# ICardValidationContext.TaskCardMetadataBinder - свойство
Объект, выполняющий действия с карточкой задания, для которой выполняется
валидация, или null, если задание завершается без данных карточки или
валидация задания не выполняется.
## __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    ICardMetadataBinder TaskCardMetadataBinder { get; set; }
VB __Копировать
     Property TaskCardMetadataBinder As ICardMetadataBinder
    	Get
    	Set
C++ __Копировать
    property ICardMetadataBinder^ TaskCardMetadataBinder {
    	ICardMetadataBinder^ get ();
    	void set (ICardMetadataBinder^ value);
    }
F# __Копировать
     abstract TaskCardMetadataBinder : ICardMetadataBinder with get, set
#### Значение свойства
[ICardMetadataBinder](T_Tessa_Cards_Metadata_ICardMetadataBinder.htm)
##  __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[ICardValidationContext -
](T_Tessa_Cards_Validation_ICardValidationContext.htm)
[Tessa.Cards.Validation - пространство имён](N_Tessa_Cards_Validation.htm)
[Tessa.Platform.ObjectSealedException]
