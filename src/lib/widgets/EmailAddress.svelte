<script lang="ts">
  interface Props {
    email: string;
  }

  let { email }: Props = $props();

  let [user, domain] = email.split('@');
  domain = domain.replace('.', ' dot ');

  const reverse = (s: string) => {
    return s.split('').reverse().join('');
  };

  const text = `${reverse(domain)} ta ${reverse(user)}`.replaceAll(
    ' ',
    '\u00A0'
  );
</script>

<bdo dir="rtl" class="user-select-none" aria-hidden="true">
  {text}
</bdo>
