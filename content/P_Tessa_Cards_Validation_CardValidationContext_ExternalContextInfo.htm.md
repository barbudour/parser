# CardValidationContext.ExternalContextInfo - свойство
Произвольно структурированная информация из внешнего контекста (например,
контекста сохранения карточки), которая может быть заполнена валидатором и
использована либо другими валидаторами, либо внешними расширениями. Когда
внешний контекст неизвестен, будет создан пустой объект, но при этом свойство
никогда не возвращает null.
## __Definition
 **Пространство имён:** [Tessa.Cards.Validation](N_Tessa_Cards_Validation.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ISerializableObject ExternalContextInfo { get; }
VB __Копировать
     Public ReadOnly Property ExternalContextInfo As ISerializableObject
    	Get
C++ __Копировать
     public:
    virtual property ISerializableObject^ ExternalContextInfo {
    	ISerializableObject^ get () sealed;
    }
F# __Копировать
     abstract ExternalContextInfo : ISerializableObject with get
    override ExternalContextInfo : ISerializableObject with get
#### Значение свойства
[ISerializableObject](T_Tessa_Platform_Storage_ISerializableObject.htm)
#### Реализации
[ICardValidationContext.ExternalContextInfo](P_Tessa_Cards_Validation_ICardValidationContext_ExternalContextInfo.htm)  
##  __См. также
#### Ссылки
[CardValidationContext - ](T_Tessa_Cards_Validation_CardValidationContext.htm)
[Tessa.Cards.Validation - пространство имён](N_Tessa_Cards_Validation.htm)
