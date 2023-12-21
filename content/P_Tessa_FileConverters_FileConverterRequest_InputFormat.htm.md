# FileConverterRequest.InputFormat - свойство
Формат преобразуемого файла. Устанавливайте значение этого свойства после
установки [Tessa.FileConverters.IFileConverterRequest.FileName].
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public string InputFormat { get; set; }
VB __Копировать
     Public Property InputFormat As String
    	Get
    	Set
C++ __Копировать
     public:
    virtual property String^ InputFormat {
    	String^ get () sealed;
    	void set (String^ value) sealed;
    }
F# __Копировать
     abstract InputFormat : string with get, set
    override InputFormat : string with get, set
#### Значение свойства
[String](https://learn.microsoft.com/dotnet/api/system.string)
#### Реализации
[IFileConverterRequest.InputFormat](P_Tessa_FileConverters_IFileConverterRequest_InputFormat.htm)  
##  __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[FileConverterRequest - ](T_Tessa_FileConverters_FileConverterRequest.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
[Tessa.Platform.ObjectSealedException]
