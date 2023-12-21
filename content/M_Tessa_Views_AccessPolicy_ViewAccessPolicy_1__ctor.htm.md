# ViewAccessPolicy<TContext> \- конструктор
Инициализирует новый экземпляр класса
[ViewAccessPolicy<TContext>](T_Tessa_Views_AccessPolicy_ViewAccessPolicy_1.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Views.AccessPolicy](N_Tessa_Views_AccessPolicy.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ViewAccessPolicy(
    	[NotNullAttribute] IAccessRule<ITessaView, TContext>[] globalRules,
    	[NotNullAttribute] IViewAccessRule<TContext>[] accessRules
    )
VB __Копировать
     Public Sub New ( 
    	<NotNullAttribute> globalRules As IAccessRule(Of ITessaView, TContext)(),
    	<NotNullAttribute> accessRules As IViewAccessRule(Of TContext)()
    )
C++ __Копировать
     public:
    ViewAccessPolicy(
    	[NotNullAttribute] array<IAccessRule<ITessaView^, TContext>^>^ globalRules, 
    	[NotNullAttribute] array<IViewAccessRule<TContext>^>^ accessRules
    )
F# __Копировать
     new : 
            [<NotNullAttribute>] globalRules : IAccessRule<ITessaView, 'TContext>[] * 
            [<NotNullAttribute>] accessRules : IViewAccessRule<'TContext>[] -> ViewAccessPolicy
#### Параметры
globalRules
[IAccessRule](T_Tessa_Views_AccessPolicy_IAccessRule_2.htm)<[ITessaView](T_Tessa_Views_ITessaView.htm),
[TContext](T_Tessa_Views_AccessPolicy_ViewAccessPolicy_1.htm)>[]
accessRules
[IViewAccessRule](T_Tessa_Views_AccessPolicy_IViewAccessRule_1.htm)<[TContext](T_Tessa_Views_AccessPolicy_ViewAccessPolicy_1.htm)>[]
## __См. также
#### Ссылки
[ViewAccessPolicy<TContext> \-
](T_Tessa_Views_AccessPolicy_ViewAccessPolicy_1.htm)
[Tessa.Views.AccessPolicy - пространство имён](N_Tessa_Views_AccessPolicy.htm)
