# IsolatedStorageHelper.ReadAllTextForApplicationAsync - метод
Считывает весь текст из текстового файла с заданными именем, расположенного в
хранилище, изолированном для пользователя и сборки.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task<string> ReadAllTextForApplicationAsync(
    	string filename
    )
VB __Копировать
     Public Shared Function ReadAllTextForApplicationAsync ( 
    	filename As String
    ) As Task(Of String)
C++ __Копировать
     public:
    static Task<String^>^ ReadAllTextForApplicationAsync(
    	String^ filename
    )
F# __Копировать
     static member ReadAllTextForApplicationAsync : 
            filename : string -> Task<string> 
#### Параметры
filename [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя текстового файла.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>  
Строкое содержимое текстового файла.
##  __См. также
#### Ссылки
[IsolatedStorageHelper - ](T_Chronos_Platform_IsolatedStorageHelper.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
