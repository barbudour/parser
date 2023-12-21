# FileConverterContext.InputExtension - свойство
Расширение для конвертируемого файла. Задаётся как расширение файла в нижнем
регистре без ведущей точки. Может быть равно null или пустой строке, если у
файла нет расширения.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public string InputExtension { get; }
VB __Копировать
     Public ReadOnly Property InputExtension As String
    	Get
C++ __Копировать
     public:
    virtual property String^ InputExtension {
    	String^ get () sealed;
    }
F# __Копировать
     abstract InputExtension : string with get
    override InputExtension : string with get
#### Значение свойства
[String](https://learn.microsoft.com/dotnet/api/system.string)
#### Реализации
[IFileConverterContext.InputExtension](P_Tessa_FileConverters_IFileConverterContext_InputExtension.htm)  
##  __Заметки
Значение свойства никогда не равно null.
## __См. также
#### Ссылки
[FileConverterContext - ](T_Tessa_FileConverters_FileConverterContext.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
