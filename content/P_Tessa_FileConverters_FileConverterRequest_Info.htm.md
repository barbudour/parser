# FileConverterRequest.Info - свойство
Дополнительная информация, передаваемая в параметры конвертации. От такой
информации не зависит вычисление хеша запроса (и идентификация похожих
операций), в отличие от данных в свойстве
[Tessa.FileConverters.IFileConverterRequest.Parameters].
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
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
[IFileConverterRequest.Info](P_Tessa_FileConverters_IFileConverterRequest_Info.htm)  
##  __Заметки
Значение свойства никогда не равно null.
## __См. также
#### Ссылки
[FileConverterRequest - ](T_Tessa_FileConverters_FileConverterRequest.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
