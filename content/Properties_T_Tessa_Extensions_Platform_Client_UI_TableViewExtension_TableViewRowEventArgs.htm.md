# TableViewRowEventArgs - свойства
##  __Свойства
[Action](P_Tessa_UI_Cards_Controls_RowEventArgs_Action.htm)|  Действие со
строкой [Row](P_Tessa_UI_Cards_Controls_RowEventArgs_Row.htm).  
(Унаследован от [RowEventArgs](T_Tessa_UI_Cards_Controls_RowEventArgs.htm))  
---|---  
[Cancel](P_Tessa_UI_Cards_Controls_RowEventArgs_Cancel.htm)|  Признак того,
что действие строки отменяется.  
(Унаследован от [RowEventArgs](T_Tessa_UI_Cards_Controls_RowEventArgs.htm))  
[CancellationToken](P_Tessa_UI_Cards_Controls_RowEventArgs_CancellationToken.htm)|
Объект, посредством которого можно отменить асинхронную задачу.  
(Унаследован от [RowEventArgs](T_Tessa_UI_Cards_Controls_RowEventArgs.htm))  
[CardModel](P_Tessa_UI_Cards_Controls_RowEventArgs_CardModel.htm)|  Модель
карточки, в которой расположена строка
[Row](P_Tessa_UI_Cards_Controls_RowEventArgs_Row.htm).  
(Унаследован от [RowEventArgs](T_Tessa_UI_Cards_Controls_RowEventArgs.htm))  
[Cell](P_Tessa_Extensions_Platform_Client_UI_TableViewExtension_TableViewRowEventArgs_Cell.htm)|
Объект, описывающий ячейку, по которой был выполнен клик, или null, если клик
был по строке снаружи ячеек или производится добавление/удаление строки без
привязки к ячейке.  
[Control](P_Tessa_Extensions_Platform_Client_UI_TableViewExtension_TableViewRowEventArgs_Control.htm)|
Контрол, в рамках которого выполняется событие.  
[Row](P_Tessa_UI_Cards_Controls_RowEventArgs_Row.htm)|  Строка карточки, с
которой производится действие.  
(Унаследован от [RowEventArgs](T_Tessa_UI_Cards_Controls_RowEventArgs.htm))  
[RowModel](P_Tessa_UI_Cards_Controls_RowEventArgs_RowModel.htm)|  Модель
строки [Row](P_Tessa_UI_Cards_Controls_RowEventArgs_Row.htm) вместе с формой,
которая только что была инициализирована, или null, если выполняется удаление
строки, при этом модель не требуется.  
(Унаследован от [RowEventArgs](T_Tessa_UI_Cards_Controls_RowEventArgs.htm))  
[RowViewModel](P_Tessa_Extensions_Platform_Client_UI_TableViewExtension_TableViewRowEventArgs_RowViewModel.htm)|
Модель строки [Row](P_Tessa_UI_Cards_Controls_RowEventArgs_Row.htm) вместе с
формой, которая только что была инициализирована, или null, если выполняется
удаление строки, при этом модель не требуется.  
[ValidationResult](P_Tessa_Extensions_Platform_Client_UI_TableViewExtension_TableViewRowEventArgs_ValidationResult.htm)|
Результат валидации строки.  
[Window](P_Tessa_UI_Cards_Controls_RowEventArgs_Window.htm)|  Окно, в котором
отображается строка, или null, если окно ещё не было инициализировано. В
событии
[RowInitializing](E_Tessa_UI_Cards_Controls_GridViewModel_RowInitializing.htm)
свойство гарантированно возвращает не null, в то время, как в событии
[RowInvoked](E_Tessa_UI_Cards_Controls_GridViewModel_RowInvoked.htm) будет
null.  
(Унаследован от [RowEventArgs](T_Tessa_UI_Cards_Controls_RowEventArgs.htm))  
##  __См. также
#### Ссылки
[TableViewRowEventArgs -
](T_Tessa_Extensions_Platform_Client_UI_TableViewExtension_TableViewRowEventArgs.htm)
[Tessa.Extensions.Platform.Client.UI.TableViewExtension - пространство
имён](N_Tessa_Extensions_Platform_Client_UI_TableViewExtension.htm)
