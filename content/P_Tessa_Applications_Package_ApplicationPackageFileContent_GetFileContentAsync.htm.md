# ApplicationPackageFileContent.GetFileContentAsync - свойство
##  __Definition
 **Пространство имён:**
[Tessa.Applications.Package](N_Tessa_Applications_Package.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Func<CancellationToken, ValueTask<Stream>> GetFileContentAsync { get; }
VB __Копировать
     Public ReadOnly Property GetFileContentAsync As Func(Of CancellationToken, ValueTask(Of Stream))
    	Get
C++ __Копировать
     public:
    property Func<CancellationToken, ValueTask<Stream^>>^ GetFileContentAsync {
    	Func<CancellationToken, ValueTask<Stream^>>^ get ();
    }
F# __Копировать
     member GetFileContentAsync : Func<CancellationToken, ValueTask<Stream>> with get
#### Значение свойства
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Stream](https://learn.microsoft.com/dotnet/api/system.io.stream)>>
##  __См. также
#### Ссылки
[ApplicationPackageFileContent -
](T_Tessa_Applications_Package_ApplicationPackageFileContent.htm)
[Tessa.Applications.Package - пространство
имён](N_Tessa_Applications_Package.htm)
