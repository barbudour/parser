# ScanFileDialogSettings.ModifyDialogActionAsync - свойство
Метод, который получает модель представления диалога
[ScanDialogViewModel](T_Tessa_Extensions_Platform_Client_ViewModels_ScanDialogViewModel.htm),
после чего может как угодно его изменить.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Scanning](N_Tessa_Extensions_Platform_Client_Scanning.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public Func<ScanDialogViewModel, CancellationToken, ValueTask> ModifyDialogActionAsync { get; set; }
VB __Копировать
     Public Property ModifyDialogActionAsync As Func(Of ScanDialogViewModel, CancellationToken, ValueTask)
    	Get
    	Set
C++ __Копировать
     public:
    property Func<ScanDialogViewModel^, CancellationToken, ValueTask>^ ModifyDialogActionAsync {
    	Func<ScanDialogViewModel^, CancellationToken, ValueTask>^ get ();
    	void set (Func<ScanDialogViewModel^, CancellationToken, ValueTask>^ value);
    }
F# __Копировать
     member ModifyDialogActionAsync : Func<ScanDialogViewModel, CancellationToken, ValueTask> with get, set
#### Значение свойства
[Func](https://learn.microsoft.com/dotnet/api/system.func-3)<[ScanDialogViewModel](T_Tessa_Extensions_Platform_Client_ViewModels_ScanDialogViewModel.htm),
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken),
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)>
##  __См. также
#### Ссылки
[ScanFileDialogSettings -
](T_Tessa_Extensions_Platform_Client_Scanning_ScanFileDialogSettings.htm)
[Tessa.Extensions.Platform.Client.Scanning - пространство
имён](N_Tessa_Extensions_Platform_Client_Scanning.htm)
