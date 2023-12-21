# NumberContext.Info - свойство
Произвольно структурированная информация, используемая при обработке события,
происходящего с номером.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ISerializableObject Info { get; }
VB __Копировать
     Public ReadOnly Property Info As ISerializableObject
    	Get
C++ __Копировать
     public:
    virtual property ISerializableObject^ Info {
    	ISerializableObject^ get () sealed;
    }
F# __Копировать
     abstract Info : ISerializableObject with get
    override Info : ISerializableObject with get
#### Значение свойства
[ISerializableObject](T_Tessa_Platform_Storage_ISerializableObject.htm)
#### Реализации
[INumberContext.Info](P_Tessa_Cards_Numbers_INumberContext_Info.htm)  
##  __Заметки
Значение свойства никогда не равно null.
## __См. также
#### Ссылки
[NumberContext - ](T_Tessa_Cards_Numbers_NumberContext.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
