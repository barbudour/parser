# FileConverterContext.OutputFilePath - свойство
Путь к выходному файлу. Может быть изменён, если приложение-конвертер записало
файл по другому пути. Не может быть равен null или пустой строке.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public string OutputFilePath { get; set; }
VB __Копировать
     Public Property OutputFilePath As String
    	Get
    	Set
C++ __Копировать
     public:
    virtual property String^ OutputFilePath {
    	String^ get () sealed;
    	void set (String^ value) sealed;
    }
F# __Копировать
     abstract OutputFilePath : string with get, set
    override OutputFilePath : string with get, set
#### Значение свойства
[String](https://learn.microsoft.com/dotnet/api/system.string)
#### Реализации
[IFileConverterContext.OutputFilePath](P_Tessa_FileConverters_IFileConverterContext_OutputFilePath.htm)  
##  __Заметки
Значение свойства никогда не равно null.
## __См. также
#### Ссылки
[FileConverterContext - ](T_Tessa_FileConverters_FileConverterContext.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
