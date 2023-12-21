# IFileConverterRequest.Parameters - свойство
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
    ISerializableObject Parameters { get; }
VB __Копировать
     ReadOnly Property Parameters As ISerializableObject
    	Get
C++ __Копировать
    property ISerializableObject^ Parameters {
    	ISerializableObject^ get ();
    }
F# __Копировать
     abstract Parameters : ISerializableObject with get
#### Значение свойства
[ISerializableObject](T_Tessa_Platform_Storage_ISerializableObject.htm)
##  __Заметки
Значение свойства никогда не равно null.
## __См. также
#### Ссылки
[IFileConverterRequest - ](T_Tessa_FileConverters_IFileConverterRequest.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
