# NumberContext.PlaceholderInfo - свойство
Информация, передаваемая в свойство IPlaceholderContext.Info при замене
плейсхолдеров в формате номера, формате последовательности или в других
случаях, когда для API номеров требуется задействовать API плейсхолдеров.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ISerializableObject PlaceholderInfo { get; }
VB __Копировать
     Public ReadOnly Property PlaceholderInfo As ISerializableObject
    	Get
C++ __Копировать
     public:
    virtual property ISerializableObject^ PlaceholderInfo {
    	ISerializableObject^ get () sealed;
    }
F# __Копировать
     abstract PlaceholderInfo : ISerializableObject with get
    override PlaceholderInfo : ISerializableObject with get
#### Значение свойства
[ISerializableObject](T_Tessa_Platform_Storage_ISerializableObject.htm)
#### Реализации
[INumberContext.PlaceholderInfo](P_Tessa_Cards_Numbers_INumberContext_PlaceholderInfo.htm)  
##  __Заметки
Значение свойства никогда не равно null.
## __См. также
#### Ссылки
[NumberContext - ](T_Tessa_Cards_Numbers_NumberContext.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
