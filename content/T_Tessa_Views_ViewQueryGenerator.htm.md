# ViewQueryGenerator - делегат
Делагат осуществляющий построение текста выражения для представления в
соответствии с метаданными viewMetadata и запросом к представлению request,
результат выполнения запроса будет помещен в буфер вывода builder
##  __Definition
 **Пространство имён:** [Tessa.Views](N_Tessa_Views.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public delegate void ViewQueryGenerator(
    	[NotNullAttribute] StringBuilder builder,
    	[NotNullAttribute] IViewMetadata viewMetadata,
    	[NotNullAttribute] ITessaViewRequest request,
    	[NotNullAttribute] IUser user,
    	[NotNullAttribute] ISession session
    )
VB __Копировать
     Public Delegate Sub ViewQueryGenerator ( 
    	<NotNullAttribute> builder As StringBuilder,
    	<NotNullAttribute> viewMetadata As IViewMetadata,
    	<NotNullAttribute> request As ITessaViewRequest,
    	<NotNullAttribute> user As IUser,
    	<NotNullAttribute> session As ISession
    )
C++ __Копировать
     public delegate void ViewQueryGenerator(
    	[NotNullAttribute] StringBuilder^ builder, 
    	[NotNullAttribute] IViewMetadata^ viewMetadata, 
    	[NotNullAttribute] ITessaViewRequest^ request, 
    	[NotNullAttribute] IUser^ user, 
    	[NotNullAttribute] ISession^ session
    )
F# __Копировать
     type ViewQueryGenerator = 
        delegate of 
            [<NotNullAttribute>] builder : StringBuilder * 
            [<NotNullAttribute>] viewMetadata : IViewMetadata * 
            [<NotNullAttribute>] request : ITessaViewRequest * 
            [<NotNullAttribute>] user : IUser * 
            [<NotNullAttribute>] session : ISession -> unit
#### Параметры
builder
[StringBuilder](https://learn.microsoft.com/dotnet/api/system.text.stringbuilder)
    Буфер вывода
viewMetadata [IViewMetadata](T_Tessa_Views_Metadata_IViewMetadata.htm)
    Метаданные представления
request [ITessaViewRequest](T_Tessa_Views_ITessaViewRequest.htm)
    Запрос к представлению
user [IUser](T_Tessa_Platform_Runtime_IUser.htm)
    Информация о пользователе
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
## __См. также
#### Ссылки
[Tessa.Views - пространство имён](N_Tessa_Views.htm)
