# FileConverterContext.RequestInfo - свойство
Информация, полученная из запроса на выполнение операции. В отличие от
свойства Request, это возвращаемое значение не равно null, причём при
отсутствии информации по запросу будет получен пустой объект.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ISerializableObject RequestInfo { get; }
VB __Копировать
     Public ReadOnly Property RequestInfo As ISerializableObject
    	Get
C++ __Копировать
     public:
    virtual property ISerializableObject^ RequestInfo {
    	ISerializableObject^ get () sealed;
    }
F# __Копировать
     abstract RequestInfo : ISerializableObject with get
    override RequestInfo : ISerializableObject with get
#### Значение свойства
[ISerializableObject](T_Tessa_Platform_Storage_ISerializableObject.htm)
#### Реализации
[IFileConverterContext.RequestInfo](P_Tessa_FileConverters_IFileConverterContext_RequestInfo.htm)  
##  __Заметки
Значение свойства никогда не равно null.
## __См. также
#### Ссылки
[FileConverterContext - ](T_Tessa_FileConverters_FileConverterContext.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
