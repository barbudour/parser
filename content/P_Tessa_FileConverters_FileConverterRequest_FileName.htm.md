# FileConverterRequest.FileName - свойство
Имя преобразуемого файла. При установке автоматически определяет и
устанавливает значение свойства
[Tessa.FileConverters.IFileConverterRequest.InputFormat].
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public string FileName { get; set; }
VB __Копировать
     Public Property FileName As String
    	Get
    	Set
C++ __Копировать
     public:
    virtual property String^ FileName {
    	String^ get () sealed;
    	void set (String^ value) sealed;
    }
F# __Копировать
     abstract FileName : string with get, set
    override FileName : string with get, set
#### Значение свойства
[String](https://learn.microsoft.com/dotnet/api/system.string)
#### Реализации
[IFileConverterRequest.FileName](P_Tessa_FileConverters_IFileConverterRequest_FileName.htm)  
##  __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[FileConverterRequest - ](T_Tessa_FileConverters_FileConverterRequest.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
[Tessa.Platform.ObjectSealedException]
