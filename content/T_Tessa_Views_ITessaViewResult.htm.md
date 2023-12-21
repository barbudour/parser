# ITessaViewResult - интерфейс
Интерфейс результатов запросов к представлению
## __Definition
 **Пространство имён:** [Tessa.Views](N_Tessa_Views.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ITessaViewResult
VB __Копировать
     Public Interface ITessaViewResult
C++ __Копировать
     public interface class ITessaViewResult
F# __Копировать
     type ITessaViewResult = interface end
##  __Свойства
[Columns](P_Tessa_Views_ITessaViewResult_Columns.htm)|  Список колонок.  
---|---  
[DataTypes](P_Tessa_Views_ITessaViewResult_DataTypes.htm)|  Список типов
данных SQL. Рекомендуется использовать
[SchemeTypes](P_Tessa_Views_ITessaViewResult_SchemeTypes.htm) для обработки
типов данных, не связанных с конкретной СУБД.  
Устарело.  
[HasTimeOut](P_Tessa_Views_ITessaViewResult_HasTimeOut.htm)|  Признак
прерывания выполнения запроса по тайм-ауту.  
[Result](P_Tessa_Views_ITessaViewResult_Result.htm)|  Колонки представления.  
[RowCount](P_Tessa_Views_ITessaViewResult_RowCount.htm)|  Количество строк,
которое доступно в запросе. Данное количество, строк является расчетным и не
всегда равно количеству строк в
[Rows](P_Tessa_Views_ITessaViewResult_Rows.htm).  
[Rows](P_Tessa_Views_ITessaViewResult_Rows.htm)|  Строки таблицы.  
[SchemeTypes](P_Tessa_Views_ITessaViewResult_SchemeTypes.htm)|  Список типов
данных.  
## __Методы
[GetColumnIndex](M_Tessa_Views_ITessaViewResult_GetColumnIndex.htm)|
Возвращает индекс колонки заданной параметром columnName или -1 если колонка
не найдена  
---|---  
## __Методы расширения
[ConvertToListViewModel](M_Tessa_UI_Views_TessaListViewHelper_ConvertToListViewModel_2.htm)|
Преобразует результат запроса к представлению в модель таблицы
[ITessaListViewViewModel](T_Tessa_UI_Controls_TessaGrid_ITessaListViewViewModel.htm)  
(Определяется [TessaListViewHelper](T_Tessa_UI_Views_TessaListViewHelper.htm))  
---|---  
##  __См. также
#### Ссылки
[Tessa.Views - пространство имён](N_Tessa_Views.htm)
