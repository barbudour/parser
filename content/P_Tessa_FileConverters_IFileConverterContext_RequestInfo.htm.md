# IFileConverterContext.RequestInfo - свойство
Информация, полученная из запроса на выполнение операции. В отличие от
свойства Request, это возвращаемое значение не равно null, причём при
отсутствии информации по запросу будет получен пустой объект.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    ISerializableObject RequestInfo { get; }
VB __Копировать
     ReadOnly Property RequestInfo As ISerializableObject
    	Get
C++ __Копировать
    property ISerializableObject^ RequestInfo {
    	ISerializableObject^ get ();
    }
F# __Копировать
     abstract RequestInfo : ISerializableObject with get
#### Значение свойства
[ISerializableObject](T_Tessa_Platform_Storage_ISerializableObject.htm)
##  __Заметки
Значение свойства никогда не равно null.
## __См. также
#### Ссылки
[IFileConverterContext - ](T_Tessa_FileConverters_IFileConverterContext.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
