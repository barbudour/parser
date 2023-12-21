# IFileConverterContext.OutputFilePath - свойство
Путь к выходному файлу. Может быть изменён, если приложение-конвертер записало
файл по другому пути. Не может быть равен null или пустой строке.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     string OutputFilePath { get; set; }
VB __Копировать
     Property OutputFilePath As String
    	Get
    	Set
C++ __Копировать
    property String^ OutputFilePath {
    	String^ get ();
    	void set (String^ value);
    }
F# __Копировать
     abstract OutputFilePath : string with get, set
#### Значение свойства
[String](https://learn.microsoft.com/dotnet/api/system.string)
##  __Заметки
Значение свойства никогда не равно null.
## __См. также
#### Ссылки
[IFileConverterContext - ](T_Tessa_FileConverters_IFileConverterContext.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
