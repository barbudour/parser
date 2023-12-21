# TessaViewFactory - делегат
Делегат фабрики создания представления
## __Definition
 **Пространство имён:** [Tessa.Views](N_Tessa_Views.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [NotNullAttribute]
    public delegate ITessaView TessaViewFactory(
    	Dbms dbms,
    	[NotNullAttribute] TessaViewModel model
    )
VB __Копировать
    <NotNullAttribute>
    Public Delegate Function TessaViewFactory ( 
    	dbms As Dbms,
    	<NotNullAttribute> model As TessaViewModel
    ) As ITessaView
C++ __Копировать
    [NotNullAttribute]
    public delegate ITessaView^ TessaViewFactory(
    	Dbms dbms, 
    	[NotNullAttribute] TessaViewModel^ model
    )
F# __Копировать
     [<NotNullAttribute>]
    type TessaViewFactory = 
        delegate of 
            dbms : Dbms * 
            [<NotNullAttribute>] model : TessaViewModel -> ITessaView
#### Параметры
dbms [Dbms](T_Tessa_Platform_Data_Dbms.htm)
    Тип базы данных
model [TessaViewModel](T_Tessa_Views_TessaViewModel.htm)
    Модель представления
#### Возвращаемое значение
[ITessaView](T_Tessa_Views_ITessaView.htm)  
Представление
##  __См. также
#### Ссылки
[Tessa.Views - пространство имён](N_Tessa_Views.htm)
