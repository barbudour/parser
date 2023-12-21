# NumberContext.SerializableInfo - свойство
Сериализуемая информация, которая может быть передана при обмене данными между
клиентом и сервером. Обычно это информация из методов, связанных с элементом
управления номерами, которую можно получить из сервера в клиентском
NumberControlResponse.Info. Запрещено использовать это свойство для хранения
несериализуемых объектов, т.к. это приведёт к ошибке при сериализации данных.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ISerializableObject SerializableInfo { get; }
VB __Копировать
     Public ReadOnly Property SerializableInfo As ISerializableObject
    	Get
C++ __Копировать
     public:
    virtual property ISerializableObject^ SerializableInfo {
    	ISerializableObject^ get () sealed;
    }
F# __Копировать
     abstract SerializableInfo : ISerializableObject with get
    override SerializableInfo : ISerializableObject with get
#### Значение свойства
[ISerializableObject](T_Tessa_Platform_Storage_ISerializableObject.htm)
#### Реализации
[INumberContext.SerializableInfo](P_Tessa_Cards_Numbers_INumberContext_SerializableInfo.htm)  
##  __Заметки
Значение свойства никогда не равно null.
## __См. также
#### Ссылки
[NumberContext - ](T_Tessa_Cards_Numbers_NumberContext.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
