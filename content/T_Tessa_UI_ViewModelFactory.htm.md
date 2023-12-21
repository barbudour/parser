# ViewModelFactory - делегат
##  __Definition
 **Пространство имён:** [Tessa.UI](N_Tessa_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public delegate IViewModel ViewModelFactory(
    	Object model,
    	ViewModelScope scope
    )
VB __Копировать
     Public Delegate Function ViewModelFactory ( 
    	model As Object,
    	scope As ViewModelScope
    ) As IViewModel
C++ __Копировать
     public delegate IViewModel^ ViewModelFactory(
    	Object^ model, 
    	ViewModelScope^ scope
    )
F# __Копировать
     type ViewModelFactory = 
        delegate of 
            model : Object * 
            scope : ViewModelScope -> IViewModel
#### Параметры
model [Object](https://learn.microsoft.com/dotnet/api/system.object)
scope [ViewModelScope](T_Tessa_UI_ViewModelScope.htm)
#### Возвращаемое значение
[IViewModel](T_Tessa_UI_IViewModel.htm)
##  __См. также
#### Ссылки
[Tessa.UI - пространство имён](N_Tessa_UI.htm)
