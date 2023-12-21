# FileConverterEventNamePolicy - конструктор
Создаёт экземпляр класса с указанием списка допустимых имён событий по
конвертации файлов для выполнения методов расширения.
## __Definition
 **Пространство имён:** [Tessa.FileConverters](N_Tessa_FileConverters.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public FileConverterEventNamePolicy(
    	params string[] eventNames
    )
VB __Копировать
     Public Sub New ( 
    	ParamArray eventNames As String()
    )
C++ __Копировать
     public:
    FileConverterEventNamePolicy(
    	... array<String^>^ eventNames
    )
F# __Копировать
     new : 
            eventNames : string[] -> FileConverterEventNamePolicy
#### Параметры
eventNames [String](https://learn.microsoft.com/dotnet/api/system.string)[]
     Список допустимых имён событий по конвертации файлов для выполнения методов расширения. Значения null недопустимы. 
## __См. также
#### Ссылки
[FileConverterEventNamePolicy -
](T_Tessa_FileConverters_FileConverterEventNamePolicy.htm)
[Tessa.FileConverters - пространство имён](N_Tessa_FileConverters.htm)
