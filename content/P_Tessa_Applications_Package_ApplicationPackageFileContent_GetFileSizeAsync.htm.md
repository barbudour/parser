# ApplicationPackageFileContent.GetFileSizeAsync - свойство
##  __Definition
 **Пространство имён:**
[Tessa.Applications.Package](N_Tessa_Applications_Package.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Func<CancellationToken, ValueTask<long>> GetFileSizeAsync { get; }
VB __Копировать
     Public ReadOnly Property GetFileSizeAsync As Func(Of CancellationToken, ValueTask(Of Long))
    	Get
C++ __Копировать
     public:
    property Func<CancellationToken, ValueTask<long long>>^ GetFileSizeAsync {
    	Func<CancellationToken, ValueTask<long long>>^ get ();
    }
F# __Копировать
     member GetFileSizeAsync : Func<CancellationToken, ValueTask<int64>> with get
#### Значение свойства
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[Int64](https://learn.microsoft.com/dotnet/api/system.int64)>>
##  __См. также
#### Ссылки
[ApplicationPackageFileContent -
](T_Tessa_Applications_Package_ApplicationPackageFileContent.htm)
[Tessa.Applications.Package - пространство
имён](N_Tessa_Applications_Package.htm)
