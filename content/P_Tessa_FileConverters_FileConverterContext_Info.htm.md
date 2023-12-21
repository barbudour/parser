# FileConverterContext.Info - свойство
Неструктурированная информация для цепочки расширений. Такая информация нигде
не сохраняется после завершения конвертации.
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
[IFileConverterContext.Info](P_Tessa_FileConverters_IFileConverterContext_Info.htm)  
##  __Заметки
Значение свойства никогда не равно null.
## __См. также
#### Ссылки
[FileConverterContext - ](T_Tessa_FileConverters_FileConverterContext.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
