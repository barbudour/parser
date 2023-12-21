# ScanPageViewModel - конструктор
Инициализирует новый экземпляр класса
[ScanPageViewModel](T_Tessa_Extensions_Platform_Client_ViewModels_ScanPageViewModel.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.ViewModels](N_Tessa_Extensions_Platform_Client_ViewModels.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public ScanPageViewModel(
    	string name,
    	BitmapSource thumbnail,
    	ITempFile model,
    	Func<ScanPageViewModel, ValueTask> deleteActionAsync
    )
VB __Копировать
     Public Sub New ( 
    	name As String,
    	thumbnail As BitmapSource,
    	model As ITempFile,
    	deleteActionAsync As Func(Of ScanPageViewModel, ValueTask)
    )
C++ __Копировать
     public:
    ScanPageViewModel(
    	String^ name, 
    	BitmapSource^ thumbnail, 
    	ITempFile^ model, 
    	Func<ScanPageViewModel^, ValueTask>^ deleteActionAsync
    )
F# __Копировать
     new : 
            name : string * 
            thumbnail : BitmapSource * 
            model : ITempFile * 
            deleteActionAsync : Func<ScanPageViewModel, ValueTask> -> ScanPageViewModel
#### Параметры
name [String](https://learn.microsoft.com/dotnet/api/system.string)
thumbnail
[BitmapSource](https://learn.microsoft.com/dotnet/api/system.windows.media.imaging.bitmapsource)
model [ITempFile](T_Tessa_Platform_IO_ITempFile.htm)
deleteActionAsync
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[ScanPageViewModel](T_Tessa_Extensions_Platform_Client_ViewModels_ScanPageViewModel.htm),
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask)>
## __См. также
#### Ссылки
[ScanPageViewModel -
](T_Tessa_Extensions_Platform_Client_ViewModels_ScanPageViewModel.htm)
[Tessa.Extensions.Platform.Client.ViewModels - пространство
имён](N_Tessa_Extensions_Platform_Client_ViewModels.htm)
