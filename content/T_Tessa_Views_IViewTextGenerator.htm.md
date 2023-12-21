# IViewTextGenerator - интерфейс
Описание интерфейса генератора текста sql запроса представления
[ITessaView](T_Tessa_Views_ITessaView.htm) по запросу к представлению
[ITessaViewRequest](T_Tessa_Views_ITessaViewRequest.htm).
## __Definition
 **Пространство имён:** [Tessa.Views](N_Tessa_Views.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IViewTextGenerator
VB __Копировать
     Public Interface IViewTextGenerator
C++ __Копировать
     public interface class IViewTextGenerator
F# __Копировать
     type IViewTextGenerator = interface end
##  __Методы
[TryGenerateAsync](M_Tessa_Views_IViewTextGenerator_TryGenerateAsync.htm)|
Осуществляет попытку генерации текста SQL запроса к представлению по запросу
request. Если представление не существует или не поддерживает генерацию текста
запроса(программные представления), то будет возвращена пустая строка.
Экземпляр представления по которому необходимо предоставить сгенерированный
текст запроса выбирается из
request.[View](P_Tessa_Views_ITessaViewRequest_View.htm).  
---|---  
## __См. также
#### Ссылки
[Tessa.Views - пространство имён](N_Tessa_Views.htm)
