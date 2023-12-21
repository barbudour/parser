# ScanDialogViewModel.GetPageTempFiles - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.ViewModels](N_Tessa_Extensions_Platform_Client_ViewModels.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public ITempFile[] GetPageTempFiles(
    	bool? isSelected = null
    )
VB __Копировать
     Public Function GetPageTempFiles ( 
    	Optional isSelected As Boolean? = Nothing
    ) As ITempFile()
C++ __Копировать
     public:
    array<ITempFile^>^ GetPageTempFiles(
    	Nullable<bool> isSelected = nullptr
    )
F# __Копировать
     member GetPageTempFiles : 
            ?isSelected : Nullable<bool> 
    (* Defaults:
            let _isSelected = defaultArg isSelected null
    *)
    -> ITempFile[] 
#### Параметры
isSelected
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>
(Optional)
#### Возвращаемое значение
[ITempFile](T_Tessa_Platform_IO_ITempFile.htm)[]
##  __См. также
#### Ссылки
[ScanDialogViewModel -
](T_Tessa_Extensions_Platform_Client_ViewModels_ScanDialogViewModel.htm)
[Tessa.Extensions.Platform.Client.ViewModels - пространство
имён](N_Tessa_Extensions_Platform_Client_ViewModels.htm)
