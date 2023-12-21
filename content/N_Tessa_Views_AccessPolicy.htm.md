# Tessa.Views.AccessPolicy - пространство имён
Организация доступа к представлениям и узлам рабочего места.
##  __Классы
[AccessPolicy<TAccessSubject,
TContext>](T_Tessa_Views_AccessPolicy_AccessPolicy_2.htm)|  Универсальный
класс политики проверки доступности объектов. Используется для проверки
наличия доступа к объекту через список правил [IAccessRule<TAccessSubject,
TMandatoryContext>](T_Tessa_Views_AccessPolicy_IAccessRule_2.htm) получаемых в
конструкторе класса. Правила доступности по умолчанию должны регистрироваться
в контейнере приложения. Базовая политика доступности с помощью контейнера
приложения поддерживает два вида правил. Правила не зависимые от субъекта
доступа и контекста должны быть реализованы как открытие обобщенные классы:
## __Пример
public class ConcreteRule<TAccessSubject, TContext> :
IAccessRule<TAccessSuject, TContext> { .... }
container.RegisterType(typeof(IAccessRule<,>), typeof(ConcreteRule<,>),
typeof(ConcreteRule<>).Name);
закрытие классы:
## __Пример
public class ConcreteRule: IAccessRule<ConcreteAccessSubject, ConcreteContext>
{ .... } container.RegisterType<IAccessRule<ConcreteAccessSubject,
ConcreteContext>, ConcreteRule>();
При получении политики IAccessPolicy<ConcreteAccessSubject, ConcreteContext>
из контейнера будут получены оба вида правил. Унаследование классы могут
использовать собственные типы правил и получать их из контейнера, через
конструктор отдельно от предыдущих двух типов и затем добавляя из в список
правил политики через [AddRules(IEnumerable<IAccessRule<TAccessSubject,
TContext>>)](M_Tessa_Views_AccessPolicy_IAccessPolicy_2_AddRules.htm) приводя
к базовому типу.  
---|---  
[AccessPolicyHelper](T_Tessa_Views_AccessPolicy_AccessPolicyHelper.htm)|
Вспомогательные методы для работы с политиками доступности  
[AccessPolicyRegistration](T_Tessa_Views_AccessPolicy_AccessPolicyRegistration.htm)|
Расширение регистрирующее зависимости необходимые для использования политики
доступности элементов.  
[AccessPolicyRuleRegistration](T_Tessa_Views_AccessPolicy_AccessPolicyRuleRegistration.htm)|
Расширение для контейнера приложения IUnityContainer осуществляющее
регистрацию в контейнере глобальных правил доступности  
[GrantAccess](T_Tessa_Views_AccessPolicy_GrantAccess.htm)|  Вспомогательные
методы для определения возможности представления доступов  
[NotNullViewMetadataRule<TContext>](T_Tessa_Views_AccessPolicy_NotNullViewMetadataRule_1.htm)|
Правило доступности проверяющее наличие метаданных в представлении  
[ViewAccessPolicy<TContext>](T_Tessa_Views_AccessPolicy_ViewAccessPolicy_1.htm)|
Политика доступности представлений. Поддерживает следующие виды правил.
Открытие обобщенные классы реализующие интерфейс правил вида
[IAccessRule<TAccessSubject,
TMandatoryContext>](T_Tessa_Views_AccessPolicy_IAccessRule_2.htm). Закрытые
класс реализующие интерфейс правил вида [IAccessRule<TAccessSubject,
TMandatoryContext>](T_Tessa_Views_AccessPolicy_IAccessRule_2.htm) с
подходящими типами. Открытие обобщенные класс реализующие интерфейса правил
[IViewAccessRule<TContext>](T_Tessa_Views_AccessPolicy_IViewAccessRule_1.htm)
Закрытые классы реализующие интерфейса правил
[IViewAccessRule<TContext>](T_Tessa_Views_AccessPolicy_IViewAccessRule_1.htm)
с подходящим контекстом  
[ViewWalker<TContext>](T_Tessa_Views_AccessPolicy_ViewWalker_1.htm)|
Осуществляет фильтрацию списка представлений согласно политике доступности.  
[WorkplaceAccessPolicy<TContext>](T_Tessa_Views_AccessPolicy_WorkplaceAccessPolicy_1.htm)|
Политика доступности элементов рабочих мест  
[WorkplaceAccessRule<TContext>](T_Tessa_Views_AccessPolicy_WorkplaceAccessRule_1.htm)|  
[WorkplaceMetadataWalker<TContext>](T_Tessa_Views_AccessPolicy_WorkplaceMetadataWalker_1.htm)|
Осуществляет обработку метаданных рабочего места в соответствии с политикой
доступности элементов рабочего места  
[WorkplaceWalkerFactory](T_Tessa_Views_AccessPolicy_WorkplaceWalkerFactory.htm)|
Фабрика создания
[IWorkplaceMetadataWalker<TMandatoryContext>](T_Tessa_Views_AccessPolicy_IWorkplaceMetadataWalker_1.htm)  
##  __Интерфейсы
[IAccessPolicy<TAccessSubject,
TContext>](T_Tessa_Views_AccessPolicy_IAccessPolicy_2.htm)|  Описание
интерфейса проверки доступности элементов типа TAccessSubject в соответствии с
правилами текущей политики доступности элементов.  
---|---  
[IAccessRule<TAccessSubject,
TMandatoryContext>](T_Tessa_Views_AccessPolicy_IAccessRule_2.htm)|  Описание
интерфейса правила доступа  
[IViewAccessPolicy<TContext>](T_Tessa_Views_AccessPolicy_IViewAccessPolicy_1.htm)|
Описание интерфейса политики доступности представлений  
[IViewAccessRule<TContext>](T_Tessa_Views_AccessPolicy_IViewAccessRule_1.htm)|
Описание интерфейса правила доступности для представления  
[IViewWalker<TContext>](T_Tessa_Views_AccessPolicy_IViewWalker_1.htm)|
Описание интерфейса для объектов реализующих фильтрацию списка представлений
согласно политики доступности
[IViewAccessPolicy<TContext>](T_Tessa_Views_AccessPolicy_IViewAccessPolicy_1.htm)  
[IWorkplaceAccessPolicy<TContext>](T_Tessa_Views_AccessPolicy_IWorkplaceAccessPolicy_1.htm)|
Описание интерфейса политики доступности для обработки метаданных раочих мест  
[IWorkplaceAccessRule<TContext>](T_Tessa_Views_AccessPolicy_IWorkplaceAccessRule_1.htm)|
Описание интерфейса правила доступности для метаданных рабочего места  
[IWorkplaceMetadataWalker<TMandatoryContext>](T_Tessa_Views_AccessPolicy_IWorkplaceMetadataWalker_1.htm)|
Описание интерфейса для объектов осуществляющих обработку метаданных рабочих
мест  
[IWorkplaceWalkerFactory](T_Tessa_Views_AccessPolicy_IWorkplaceWalkerFactory.htm)|
Фабрика создания объекта осуществляющего обход дерева метаданных рабочего
места в соответствии с политикой доступности  
## __Делегаты
[AccessRuleExecutor<TAccessSubject,
TContext>](T_Tessa_Views_AccessPolicy_AccessRuleExecutor_2.htm)|  Осуществляет
выполнение правил проверки доступности объекта  
---|---
