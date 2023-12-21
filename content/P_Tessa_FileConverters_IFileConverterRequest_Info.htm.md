# IFileConverterRequest.Info - свойство
Дополнительная информация, передаваемая в параметры конвертации. От такой
информации не зависит вычисление хеша запроса (и идентификация похожих
операций), в отличие от данных в свойстве
[Tessa.FileConverters.IFileConverterRequest.Parameters].
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    ISerializableObject Info { get; }
VB __Копировать
     ReadOnly Property Info As ISerializableObject
    	Get
C++ __Копировать
    property ISerializableObject^ Info {
    	ISerializableObject^ get ();
    }
F# __Копировать
     abstract Info : ISerializableObject with get
#### Значение свойства
[ISerializableObject](T_Tessa_Platform_Storage_ISerializableObject.htm)
##  __Заметки
Значение свойства никогда не равно null.
## __См. также
#### Ссылки
[IFileConverterRequest - ](T_Tessa_FileConverters_IFileConverterRequest.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
