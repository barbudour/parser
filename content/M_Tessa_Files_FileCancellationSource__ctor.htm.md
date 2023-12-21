# FileCancellationSource - конструктор
Создаёт экземпляр класса с указанием функции, создающей объект
[CancellationTokenSource](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtokensource).
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public FileCancellationSource(
    	Func<CancellationTokenSource> tokenSourceFunc = null
    )
VB __Копировать
     Public Sub New ( 
    	Optional tokenSourceFunc As Func(Of CancellationTokenSource) = Nothing
    )
C++ __Копировать
     public:
    FileCancellationSource(
    	Func<CancellationTokenSource^>^ tokenSourceFunc = nullptr
    )
F# __Копировать
     new : 
            ?tokenSourceFunc : Func<CancellationTokenSource> 
    (* Defaults:
            let _tokenSourceFunc = defaultArg tokenSourceFunc null
    *)
    -> FileCancellationSource
#### Параметры
tokenSourceFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-1)<[CancellationTokenSource](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtokensource)>
(Optional)
     Функция, создающая объект [CancellationTokenSource](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtokensource), или null, если объект будет создан конструктором по умолчанию. 
## __См. также
#### Ссылки
[FileCancellationSource - ](T_Tessa_Files_FileCancellationSource.htm)
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
