# ICardValidationContext.MainCardMetadataBinder - свойство
Объект, выполняющий действия с основной карточкой, для которой выполняется
валидация.
##  __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    ICardMetadataBinder MainCardMetadataBinder { get; set; }
VB __Копировать
     Property MainCardMetadataBinder As ICardMetadataBinder
    	Get
    	Set
C++ __Копировать
    property ICardMetadataBinder^ MainCardMetadataBinder {
    	ICardMetadataBinder^ get ();
    	void set (ICardMetadataBinder^ value);
    }
F# __Копировать
     abstract MainCardMetadataBinder : ICardMetadataBinder with get, set
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
