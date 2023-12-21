# Tessa.UI.Cards.Editors - пространство имён
Вспомогательные классы и элементы управления для редактирования типов
карточек.
##  __Классы
[CardGridEditorColumnViewModel](T_Tessa_UI_Cards_Editors_CardGridEditorColumnViewModel.htm)|  
---|---  
[CardGridEditorRowViewModel](T_Tessa_UI_Cards_Editors_CardGridEditorRowViewModel.htm)|  
[CardPreviewViewModel](T_Tessa_UI_Cards_Editors_CardPreviewViewModel.htm)|  
[ConstantValueEditorViewModel](T_Tessa_UI_Cards_Editors_ConstantValueEditorViewModel.htm)|  
[ContainerEditorViewModel](T_Tessa_UI_Cards_Editors_ContainerEditorViewModel.htm)|
Редактор контрола "Контейнер".  
[ControlEditorViewModel](T_Tessa_UI_Cards_Editors_ControlEditorViewModel.htm)|  
[ControlEditorWithNestedWindowViewModel](T_Tessa_UI_Cards_Editors_ControlEditorWithNestedWindowViewModel.htm)|  
[EmptyEditorViewModel](T_Tessa_UI_Cards_Editors_EmptyEditorViewModel.htm)|
Редактор-заглушка. Может использоваться в случае, если надо возвратить
редактор [IEditorViewModel](T_Tessa_UI_Cards_IEditorViewModel.htm) при
отсутствии редактируемых свойств.  
[LazyEditorModel](T_Tessa_UI_Cards_Editors_LazyEditorModel.htm)|  Объект,
используемый для отложенной инициализации объекта редактора
[IEditorViewModel](T_Tessa_UI_Cards_IEditorViewModel.htm). Применяется в
редакторе типов карточек для элементов интерфейса, для которых используются
привязки Binding.  
[LazyEditorModel<T>](T_Tessa_UI_Cards_Editors_LazyEditorModel_1.htm)|  Объект,
используемый для отложенной инициализации объектов UI (моделей представления
или их коллекций). Применяется в редакторе типов карточек для элементов
интерфейса, для которых используются привязки Binding.  
[PropertyGrid](T_Tessa_UI_Cards_Editors_PropertyGrid.htm)|  Вспомогательный
класс, содержащий метод создания модели представления для редактирования
свойств объекта с настройками.  
[PropertyGridEnumItem](T_Tessa_UI_Cards_Editors_PropertyGridEnumItem.htm)|
Элемент списка для выбора значения.  
[PropertyGridHelper](T_Tessa_UI_Cards_Editors_PropertyGridHelper.htm)|
Вспомогательные методы для создания
[PropertyGrid](T_Tessa_UI_Cards_Editors_PropertyGrid.htm).  
[PropertyGridItem](T_Tessa_UI_Cards_Editors_PropertyGridItem.htm)|  Класс,
описывающий редактируемое посредством
[PropertyGrid](T_Tessa_UI_Cards_Editors_PropertyGrid.htm) свойство объекта с
настройками.  
[PropertyGridItemViewModel](T_Tessa_UI_Cards_Editors_PropertyGridItemViewModel.htm)|
Модель представления для элемента управления и соответствующего ему названия
поля, размещаемых в [PropertyGrid](T_Tessa_UI_Cards_Editors_PropertyGrid.htm).  
[PropertyGridPhysicalColumnsWithSectionType](T_Tessa_UI_Cards_Editors_PropertyGridPhysicalColumnsWithSectionType.htm)|
Тип элемента управления, выполняющего редактирование в объекте с настройками
списка из нескольких физических колонок единственной секции в рамках
[PropertyGrid](T_Tessa_UI_Cards_Editors_PropertyGrid.htm).  
[PropertyGridSelectorSettings](T_Tessa_UI_Cards_Editors_PropertyGridSelectorSettings.htm)|
Настройки для элемента управления, выполняющего редактирование списка таблиц и
колонок.  
[PropertyGridTypes](T_Tessa_UI_Cards_Editors_PropertyGridTypes.htm)|
Вспомогательные методы для создания типов элементов управления, используемых
для редактирования определённых настроек посредством
[PropertyGrid](T_Tessa_UI_Cards_Editors_PropertyGrid.htm).  
[TabControlEditorViewModel](T_Tessa_UI_Cards_Editors_TabControlEditorViewModel.htm)|  
[TabItemEditorViewModel](T_Tessa_UI_Cards_Editors_TabItemEditorViewModel.htm)|  
[TabItemEditorViewModelCollection](T_Tessa_UI_Cards_Editors_TabItemEditorViewModelCollection.htm)|  
[TextStyleEditorHelper](T_Tessa_UI_Cards_Editors_TextStyleEditorHelper.htm)|  
[ViewStorageEditorViewModel](T_Tessa_UI_Cards_Editors_ViewStorageEditorViewModel.htm)|
Редактор, отображающий хранилище заданного объекта Dictionary<string, object>.  
## __Интерфейсы
[INestedControlProvider](T_Tessa_UI_Cards_Editors_INestedControlProvider.htm)|
Объект, предоставляющий метод для добавления контролов, вложенных в объект
(обычно, в блок).  
---|---  
[IPropertyGridType](T_Tessa_UI_Cards_Editors_IPropertyGridType.htm)|  Тип
элемента управления, посредством которого выполняется редактирование объекта с
настройками в рамках
[PropertyGrid](T_Tessa_UI_Cards_Editors_PropertyGrid.htm).  
## __Перечисления
[PropertyGridControlType](T_Tessa_UI_Cards_Editors_PropertyGridControlType.htm)|
Тип элемента управления, который строится через PropertyGrid.  
---|---
