# IsolatedStorageHelper.WriteAllTextForApplicationAsync - метод
Записывает весь текст в текстовый файл с заданным именем, расположенный в
хранилище, изолированном для пользователя и сборки.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static Task WriteAllTextForApplicationAsync(
    	string filename,
    	string text
    )
VB __Копировать
     Public Shared Function WriteAllTextForApplicationAsync ( 
    	filename As String,
    	text As String
    ) As Task
C++ __Копировать
     public:
    static Task^ WriteAllTextForApplicationAsync(
    	String^ filename, 
    	String^ text
    )
F# __Копировать
     static member WriteAllTextForApplicationAsync : 
            filename : string * 
            text : string -> Task 
#### Параметры
filename [String](https://learn.microsoft.com/dotnet/api/system.string)
    Имя текстового файла.
text [String](https://learn.microsoft.com/dotnet/api/system.string)
    Строкое содержимое текстового файла.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
##  __См. также
#### Ссылки
[IsolatedStorageHelper - ](T_Chronos_Platform_IsolatedStorageHelper.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
