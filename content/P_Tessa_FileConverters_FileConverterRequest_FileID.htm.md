# FileConverterRequest.FileID - свойство
Идентификатор преобразуемого файла.
##  __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Guid FileID { get; set; }
VB __Копировать
     Public Property FileID As Guid
    	Get
    	Set
C++ __Копировать
     public:
    virtual property Guid FileID {
    	Guid get () sealed;
    	void set (Guid value) sealed;
    }
F# __Копировать
     abstract FileID : Guid with get, set
    override FileID : Guid with get, set
#### Значение свойства
[Guid](https://learn.microsoft.com/dotnet/api/system.guid)
#### Реализации
[IFileConverterRequest.FileID](P_Tessa_FileConverters_IFileConverterRequest_FileID.htm)  
##  __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[FileConverterRequest - ](T_Tessa_FileConverters_FileConverterRequest.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
[Tessa.Platform.ObjectSealedException]
