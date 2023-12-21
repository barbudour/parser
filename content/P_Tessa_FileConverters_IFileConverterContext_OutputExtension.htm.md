# IFileConverterContext.OutputExtension - свойство
Расширение для выходного формата файла. Задаётся как расширение файла в нижнем
регистре без ведущей точки. Может быть равно null или пустой строке, если у
файла нет расширения.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     string OutputExtension { get; }
VB __Копировать
     ReadOnly Property OutputExtension As String
    	Get
C++ __Копировать
    property String^ OutputExtension {
    	String^ get ();
    }
F# __Копировать
     abstract OutputExtension : string with get
#### Значение свойства
[String](https://learn.microsoft.com/dotnet/api/system.string)
##  __Заметки
Значение свойства никогда не равно null.
## __См. также
#### Ссылки
[IFileConverterContext - ](T_Tessa_FileConverters_IFileConverterContext.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
