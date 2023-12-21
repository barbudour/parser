# IRepository<TGetRequest, TChangeRequest, TResponse> \- интерфейс
Интерфейс хранилища объектов
## __Definition
 **Пространство имён:** [Tessa.Views](N_Tessa_Views.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IRepository<in TGetRequest, in TChangeRequest, TResponse>
VB __Копировать
     Public Interface IRepository(Of In TGetRequest, In TChangeRequest, TResponse)
C++ __Копировать
    generic<typename TGetRequest, typename TChangeRequest, typename TResponse>
    public interface class IRepository
F# __Копировать
     type IRepository<'TGetRequest, 'TChangeRequest, 'TResponse> = interface end
#### Параметры типа
TGetRequest
     Тип запроса к репозиторию на получение элементов 
TChangeRequest
     Тип запроса к репозиторию на изменение элементов 
TResponse
     Тип ответа репозитория на запроса получения элементов 
## __Методы
[ChangeAsync](M_Tessa_Views_IRepository_3_ChangeAsync.htm)|  Осуществляет
изменение элементов хранилища  
---|---  
[DeleteAsync](M_Tessa_Views_IRepository_3_DeleteAsync.htm)|  Удаляет элементы
из хранилища  
[GetAsync](M_Tessa_Views_IRepository_3_GetAsync.htm)|  Возвращает элементы из
хранилища  
[ImportAsync](M_Tessa_Views_IRepository_3_ImportAsync.htm)|  Осуществляет
пакетное добавление списка элементов  
[NewAsync](M_Tessa_Views_IRepository_3_NewAsync.htm)|  Осуществляет создание
новых элементов в хранилище  
## __См. также
#### Ссылки
[Tessa.Views - пространство имён](N_Tessa_Views.htm)
