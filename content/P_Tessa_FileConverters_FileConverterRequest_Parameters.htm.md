# FileConverterRequest.Parameters - свойство
Дополнительная информация, передаваемая в параметры конвертации, которая
влияет на вычисление хеша запроса. Файлы, сгенерированные с разными
параметрами, могут конвертироваться параллельно и могут сохраняться в кэш
одновременно. Если параметры идентичны (а также свойства VersionID, EventName
и OutputFormat), то система считает запросы идентичными, выполнит конвертацию
ровно один раз и вернёт результат из кэша.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ISerializableObject Parameters { get; }
VB __Копировать
     Public ReadOnly Property Parameters As ISerializableObject
    	Get
C++ __Копировать
     public:
    virtual property ISerializableObject^ Parameters {
    	ISerializableObject^ get () sealed;
    }
F# __Копировать
     abstract Parameters : ISerializableObject with get
    override Parameters : ISerializableObject with get
#### Значение свойства
[ISerializableObject](T_Tessa_Platform_Storage_ISerializableObject.htm)
#### Реализации
[IFileConverterRequest.Parameters](P_Tessa_FileConverters_IFileConverterRequest_Parameters.htm)  
##  __Заметки
Значение свойства никогда не равно null.
## __См. также
#### Ссылки
[FileConverterRequest - ](T_Tessa_FileConverters_FileConverterRequest.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
