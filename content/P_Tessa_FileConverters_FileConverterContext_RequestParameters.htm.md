# FileConverterContext.RequestParameters - свойство
Параметры, полученные из запроса на выполнение операции, которые влияют на
вычисление хеша запроса. Файлы, сгенерированные с разными параметрами, могут
конвертироваться параллельно и могут сохраняться в кэш одновременно. В отличие
от свойства Request, это возвращаемое значение не равно null, причём при
отсутствии информации по запросу будет получен пустой объект.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ISerializableObject RequestParameters { get; }
VB __Копировать
     Public ReadOnly Property RequestParameters As ISerializableObject
    	Get
C++ __Копировать
     public:
    virtual property ISerializableObject^ RequestParameters {
    	ISerializableObject^ get () sealed;
    }
F# __Копировать
     abstract RequestParameters : ISerializableObject with get
    override RequestParameters : ISerializableObject with get
#### Значение свойства
[ISerializableObject](T_Tessa_Platform_Storage_ISerializableObject.htm)
#### Реализации
[IFileConverterContext.RequestParameters](P_Tessa_FileConverters_IFileConverterContext_RequestParameters.htm)  
##  __Заметки
Значение свойства никогда не равно null.
## __См. также
#### Ссылки
[FileConverterContext - ](T_Tessa_FileConverters_FileConverterContext.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
