# FileConverterRequest.VersionID - свойство
Идентификатор версии преобразуемого файла. Значение используется для
вычисления хеша запроса.
##  __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Guid VersionID { get; set; }
VB __Копировать
     Public Property VersionID As Guid
    	Get
    	Set
C++ __Копировать
     public:
    virtual property Guid VersionID {
    	Guid get () sealed;
    	void set (Guid value) sealed;
    }
F# __Копировать
     abstract VersionID : Guid with get, set
    override VersionID : Guid with get, set
#### Значение свойства
[Guid](https://learn.microsoft.com/dotnet/api/system.guid)
#### Реализации
[IFileConverterRequest.VersionID](P_Tessa_FileConverters_IFileConverterRequest_VersionID.htm)  
##  __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[FileConverterRequest - ](T_Tessa_FileConverters_FileConverterRequest.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
[Tessa.Platform.ObjectSealedException]
