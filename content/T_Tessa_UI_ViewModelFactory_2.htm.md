# ViewModelFactory<TModel, TViewModel> \- делегат
##  __Definition
 **Пространство имён:** [Tessa.UI](N_Tessa_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public delegate TViewModel ViewModelFactory<TModel, TViewModel>(
    	TModel model,
    	ViewModelScope scope
    )
VB __Копировать
     Public Delegate Function ViewModelFactory(Of TModel, TViewModel) ( 
    	model As TModel,
    	scope As ViewModelScope
    ) As TViewModel
C++ __Копировать
     generic<typename TModel, typename TViewModel>
    public delegate TViewModel ViewModelFactory(
    	TModel model, 
    	ViewModelScope^ scope
    )
F# __Копировать
     type ViewModelFactory = 
        delegate of 
            model : 'TModel * 
            scope : ViewModelScope -> 'TViewModel
#### Параметры
model TModel
scope [ViewModelScope](T_Tessa_UI_ViewModelScope.htm)
#### Параметры типа
TModel
TViewModel
#### Возвращаемое значение
TViewModel
##  __См. также
#### Ссылки
[Tessa.UI - пространство имён](N_Tessa_UI.htm)
